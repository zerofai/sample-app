package main

import (
	"encoding/json"
	"fmt"
	"net/http"
	"os"
	"strconv"
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
	http.HandleFunc("/v1/flw", getWeather)
	http.HandleFunc("/", fallback)

	serverAddr := fmt.Sprintf(":%d", servicePort)
	fmt.Printf("Listening on port %d...\n", servicePort)
	http.ListenAndServe(serverAddr, nil)
}

func getWeather(w http.ResponseWriter, r *http.Request) {
	weatherAPIURL := "https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=flw&lang=en"
	response, err := http.Get(weatherAPIURL)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	defer response.Body.Close()

	var weather map[string]interface{}
	err = json.NewDecoder(response.Body).Decode(&weather)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	json.NewEncoder(w).Encode(weather)
}

func fallback(w http.ResponseWriter, r *http.Request) {
	message := map[string]string{"message": "Sorry, please use the right endpoint"}
	json.NewEncoder(w).Encode(message)
}
