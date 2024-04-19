package main

import (
	"database/sql"
	"encoding/json"
	"fmt"
	"math/rand"
	"net/http"
	"os"
	"strconv"
	"time"

	_ "github.com/go-sql-driver/mysql"
)

func main() {
	servicePortStr := os.Getenv("containerPort")
	servicePort := 5002 // Default port value

	if servicePortStr != "" {
		var err error
		servicePort, err = strconv.Atoi(servicePortStr)
		if err != nil {
			fmt.Println("Error converting servicePort to int:", err)
			servicePort = 5002 // Revert to default port value
		}
	}
	http.HandleFunc("/v1/name", getRandomName)
	http.HandleFunc("/", fallback)

	serverAddr := fmt.Sprintf(":%d", servicePort)
	fmt.Printf("Listening on port %d...\n", servicePort)
	http.ListenAndServe(serverAddr, nil)
}

func getRandomName(w http.ResponseWriter, r *http.Request) {
	dbHost := os.Getenv("dbhost")
	username := os.Getenv("username")
	password := os.Getenv("password")

	db, err := sql.Open("mysql", fmt.Sprintf("%s:%s@tcp(%s)/your_database", username, password, dbHost))
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	defer db.Close()

	rows, err := db.Query("SELECT First, Last FROM names")
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	defer rows.Close()

	var firstNames, lastNames []string
	for rows.Next() {
		var firstName, lastName string
		if err := rows.Scan(&firstName, &lastName); err != nil {
			http.Error(w, err.Error(), http.StatusInternalServerError)
			return
		}
		firstNames = append(firstNames, firstName)
		lastNames = append(lastNames, lastName)
	}

	rand.Seed(time.Now().UnixNano())
	randomFirstName := firstNames[rand.Intn(len(firstNames))]
	randomLastName := lastNames[rand.Intn(len(lastNames))]

	fmt.Fprintf(w, "%s %s", randomFirstName, randomLastName)
}

func fallback(w http.ResponseWriter, r *http.Request) {
	message := map[string]string{"message": "Sorry, please use the right endpoint"}
	json.NewEncoder(w).Encode(message)
}
