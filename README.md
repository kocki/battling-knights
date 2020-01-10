# Battling Knigts

Solution covers assumptions of challenge and adds some extensions for
better track game run. There is 95% test coverage, but I think, it would be
good to fill missed cases with unittests.

There is some overload with attributes, but reducing that logic could result
with lower performance if we decide to play using bigger board or more military.

I think, that would be easy to develop another features with my base, eg: swap
item if knight meet better one, maybe raise knight power according to win attack
or defence and so on.

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
    pytest --cov=battling_knights --cov-report=term-missing
    ```
