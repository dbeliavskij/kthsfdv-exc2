# Exercise 2 of KTH Formula Student - Driverless, Software Skill Training
## Functionality
3 different plotting modes:
1. Plot function for t equal from 0 to 2 (default mode)
2. Plot function for user-defined t
3. Real-time function plotting

## How to use
Start a program by running:
```python kthfsdv_exc2.py```
This will run a program in a default mode

Program accepts additional command-line arguments:
`-s start_number stop_number number_of_samples` will plot a function over defined range starting from `start_number` to `stop_number` with `number_of_samples` in between
`-t` will start a program in real-time plotting mode
`-d` starts a program in default mode

## Packages required to run a program
1. Matplotlib
2. Numpy

## Possible improvements
1. Command-line interface which lets you run program in different modes after starting it (no need to close program each time)
2. Additional error handling
3. Possibility to start real-time plotting after stopping it with Ctrl-C
4. Stopping real-time plotting with another keystroke (for example 'p')
5. Create requirements.txt
