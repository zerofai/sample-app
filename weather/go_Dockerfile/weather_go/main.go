package main

import (
 "encoding/json"
 "net/http"
)

func main() {
 http.HandleFunc("/v1/flw", getWeather)
 http.HandleFunc("/", fallback)

 http.ListenAndServe(":5002", nil)
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
