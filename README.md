# Exercise 1 of KTH Formula Student - Driverless, Software Skill Training
## Functionality
3 different plotting modes:
1. Plot function for t equal from 0 to 2 (default mode)
2. Plot function for user-defined t
3. Real-time function plotting

## How to use
Start a programm by running:
```python kthfsdv_exc2.py```
This will run a programm in a default mode

Programm accepts additional command-line arguments:
`-s start_number stop_number number_of_samples` will plot a function over defined range starting from `start_number` to `stop_number` with `number_of_samples` in between
`-t` will start a programm in real-time plotting mode
`-d` starts a programm in default mode

## Packages required to run a programm
1. Matplotlib
2. Numpy

## Posible improvements
1. Command-line interface which lets you run programm in different modes after starting it (no need to close programm each time)
2. Additional error handling
3. Possibility to start real-time plotting after stopping it with Ctrl-C
4. Stopping real-time plotting with another keystroke (for example 'p')
5. Create requirements.txt