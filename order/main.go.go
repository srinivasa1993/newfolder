// Go app (order_service/main.go)
func placeOrder(w http.ResponseWriter, r *http.Request) {
    json.NewEncoder(w).Encode(map[string]string{"status": "order placed"})
}

