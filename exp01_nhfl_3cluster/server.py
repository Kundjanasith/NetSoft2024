import flwr as fl

strategy = fl.server.strategy.FedAvg(
    fraction_fit=1,  # Sample 10% of available clients for the next round
    min_fit_clients=10,
    min_available_clients=10,  # Minimum number of clients that need to be connected to the server before a training round can start
)
fl.server.start_server(config=fl.server.ServerConfig(num_rounds=101),strategy=strategy)
