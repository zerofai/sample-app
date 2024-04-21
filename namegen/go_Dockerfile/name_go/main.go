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
	servicePort := 5004 // Default port value

	if servicePortStr != "" {
		var err error
		servicePort, err = strconv.Atoi(servicePortStr)
		if err != nil {
			fmt.Println("Error converting servicePort to int:", err)
			servicePort = 5004 // Revert to default port value
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

	db, err := sql.Open("mysql", fmt.Sprintf("%s:%s@tcp(%s)/names", username, password, dbHost))
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	defer db.Close()

	rand.Seed(time.Now().UnixNano())

	var countFirst, countLast int
	var randomFirstName, randomLastName string

	// Get the total count of First names
	err = db.QueryRow("SELECT COUNT(First) FROM firstname WHERE First IS NOT NULL").Scan(&countFirst)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	// Select a random First name
	randomIndexFirst := rand.Intn(countFirst)
	err = db.QueryRow(fmt.Sprintf("SELECT First FROM firstname WHERE First IS NOT NULL LIMIT %d, 1", randomIndexFirst)).Scan(&randomFirstName)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

// Get the total count of Last names
	err = db.QueryRow("SELECT COUNT(Last) FROM lastname WHERE Last IS NOT NULL").Scan(&countLast)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

// Select a random Last name
	randomIndexLast := rand.Intn(countLast)
	err = db.QueryRow(fmt.Sprintf("SELECT Last FROM lastname WHERE Last IS NOT NULL LIMIT %d, 1", randomIndexLast)).Scan(&randomLastName)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	fmt.Fprintf(w, "%s %s", randomFirstName, randomLastName)
}

func fallback(w http.ResponseWriter, r *http.Request) {
	message := map[string]string{"message": "Sorry, please use the right endpoint"}
	json.NewEncoder(w).Encode(message)
}
