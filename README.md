# Weather Station Observer Pattern

This project demonstrates the Observer design pattern using a Weather Station scenario in Python. The Weather Station (`WeatherStation`) notifies various displays (observers) about changes in temperature.

## Project Structure

- `main.py`: The main Python script implementing the Observer pattern.
- `Dockerfile`: Docker configuration file to build and run the project in a container.

## Prerequisites

- [Docker](https://www.docker.com/get-started) installed on your system.

## Running the Application with Docker

Follow these steps to build and run the application using Docker:

1. **Build the Docker Image**

   Open a terminal in the project directory and run:

   ```bash
   docker build -t weather_station_app .
    ```
2. **Run the Docker Container**

   Run the Docker container using the following command:

   ```bash
   docker run -it --rm weather_station_app
   ```

