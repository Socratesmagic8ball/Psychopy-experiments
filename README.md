# 1-Minute Character Reaction Time Challenge

## Project Overview
This repository contains a behavioral experiment developed using **PsychoPy**. The project is designed as a high-speed "1-Minute Challenge" to measure participant reaction times and accuracy in a character-recognition task. The experiment features an adaptive difficulty level where the inter-stimulus interval decreases over time to test the limits of cognitive processing speed.

## Task Design
The experiment utilizes three iconic characters, each mapped to a specific keyboard response:
* **Hello Kitty**: Left Arrow Key
* **Courage the Cowardly Dog**: Right Arrow Key
* **Bugs Bunny**: Up Arrow Key

### Experimental Flow:
1.  **Instruction Screen**: Displays the key mappings and experiment rules.
2.  **The Trial Loop**: Characters appear randomly for 60 seconds.
3.  **Adaptive Speed**: The "wait time" between stimuli starts at 1 second and decreases by 0.05 seconds after every trial, forcing the participant to react faster as the experiment progresses.
4.  **Feedback**: Upon completion, the participant receives an instant summary of their total trials, correct responses, accuracy percentage, and average reaction time.

## Technical Features
* **Data Logging**: Automated saving of participant metadata, reaction times, and accuracy to `.csv` and `.log` files using PsychoPy's `ExperimentHandler`.
* **GUI Integration**: Custom dialog box for participant name and session number entry at startup.
* **Statistical Calculation**: Real-time computation of performance metrics using `NumPy`.

## Implementation Details
* **Language**: Python
* **Framework**: PsychoPy
* **Supporting Libraries**: NumPy, Random, Time

## Requirements
To run the experiment, ensure you have PsychoPy installed:
```bash
pip install psychopy
