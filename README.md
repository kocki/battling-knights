# Battling Knigts

## Requires
    
* Python (3.7 testd)
* pytests to run tests

* suggested to set up virtual env

## Run

1. Pattern: 
    
    ```shell script
    ./battle.py scenario_file [animation] [report]
    ```
   
   Outputs:
   * JSON by default
   * user friendly report when `animation` in args

2. Challenge requirement
    
    ```shell script
    ./battle.py scenario_file.txt > final_state.json
    ```
   
3. Run with semi-animation:
    
    ```shell script
    ./battle.py scenario_file.txt animation
    ```

4. Run with semi-animation and board style report (knights shows their last position):
    
    ```shell script
    ./battle.py scenario_file.txt animation report
    ```

## Tests

1. Install requirements: 
    
    ```shell script
    pip install -r requirements_dev.txt
    ```

2. Run tests

    ```shell script
    pytest
    ```

3. Run tests with coverage report: 
    
    ```shell script
    pytest --cov=battle_knights --cov-report=term-missing
    ```
