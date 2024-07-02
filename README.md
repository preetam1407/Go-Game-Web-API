
# Go Game Score Calculation API

This project is a web API developed with Flask to calculate the maximum number of draws that could have occurred in a series of Go games played by three friends, given their points.

## Setup

To run this project locally, you'll need to set up a Python environment. Follow the steps below:

1. **Clone the repository**
   ```bash
   git clone https://github.com/preetam1407/Go-Game-Web-API.git
   cd Go-Game-Web-API
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

   This will start the Flask server.


## Logic Implementation
The core of this API is the `calculate_max_draws` function, which determines the maximum possible number of draws based on the players' scores. Here is a breakdown of the logic:

- If the sum of points is odd, then it is impossible to get a result.
- If the sum of points is even:
  - If `p1 + p2` is greater than or equal to `p3`, then we can utilize all points in draws, resulting in a maximum draw calculation of `(p1 + p2 + p3) / 2`.
  - If `p1 + p2` is less than `p3`, then the sum `p1 + p2` will exhaust all points available for draws, with the remaining points accounting for the wins of `p3`. Thus, the answer will be `p1 + p2`.


## Usage

The API is accessible via the endpoint `/:p1/:p2/:p3` where `p1`, `p2`, and `p3` are the points of the three players in non-decreasing order. 

Assume the base URL is `http://127.0.0.1:5000/`
### Examples

- **Get maximum draws for scores 0, 0, 0. by changing the base URL to**
  ```bash
  http://127.0.0.1:5000/0/0/0
  ```

- **Get maximum draws for scores 1, 1, 2. using curl.**
  ```bash
  curl http://127.0.0.1:5000/1/1/2
  ```

## Testing

To run the unit tests for the API, execute:

```bash
python testing.py
```

## API Documentation

This API accepts GET requests at `/:p1/:p2/:p3` and returns a JSON object with the maximum number of draws that could have occurred among the players. If the scores are not valid, the API returns a JSON object with `-1`.

### Responses

- **Valid scores**:
  ```json
  { "max_draws": 6 }
  ```

- **Invalid scores**:
  ```json
  { "max_draws": -1 }
  ```

