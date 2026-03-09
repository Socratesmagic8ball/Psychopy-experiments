from psychopy import visual, core, event, data, gui
import random
import time
import numpy as np  # Added for easy averaging

# 1. Pop-up to enter Participant Name/Number
exp_info = {'Participant': '', 'Session': '001'}
dlg = gui.DlgFromDict(dictionary=exp_info, title='Reaction Time Task')
if not dlg.OK: core.quit() 

# 2. Setup Data Saving
filename = f"data_{exp_info['Participant']}_{time.strftime('%Y%m%d_%H%M%S')}"
this_exp = data.ExperimentHandler(name='reactiontime_Study', extraInfo=exp_info, dataFileName=filename)

# 3. Setup Window and Stimuli
win = visual.Window([1000, 700], color="white", units="pix")
stim_list = [
    {'image': 'hello kitty.png', 'key': 'left', 'label': 'Hello Kitty'},
    {'image': 'courage the cowardly dog.png', 'key': 'right', 'label': 'Courage'},
    {'image': 'bugs bunny.png', 'key': 'up', 'label': 'Bugs Bunny'}
]

# 4. Instructions
instr = visual.TextStim(win, color="black", text=(
    "1-MINUTE CHALLENGE\n\n"
    "LEFT: Hello Kitty | RIGHT: Courage the cowardly Dog   |   UP: Bugs bunny\n\n"
    "Careful: It gets faster!\n\n"
    "Press any key to start."
))
instr.draw()
win.flip()
event.waitKeys()

# 5. Timer and Loop
session_duration = 60 
session_timer = core.CountdownTimer(session_duration)
rt_clock = core.Clock()

# --- Lists to store stats for immediate display ---
all_rts = []
correct_count = 0
total_trials = 0

while session_timer.getTime() > 0:
    time_passed = session_duration - session_timer.getTime()
    current_wait = max(0.5, 2.0 - (time_passed / 40.0)) 
    
    win.flip() 
    core.wait(current_wait)
    
    trial = random.choice(stim_list)
    img_stim = visual.ImageStim(win, image=trial['image'], size=(400, 400))
    
    img_stim.draw()
    win.flip()
    rt_clock.reset() 
    
    keys = event.waitKeys(keyList=['left', 'right', 'up', 'escape'], timeStamped=rt_clock)
    
    if keys:
        key_name, rt = keys[0]
        if key_name == 'escape': break
        
        is_correct = 1 if key_name == trial['key'] else 0
        
        # --- Update Stats ---
        all_rts.append(rt)
        total_trials += 1
        if is_correct:
            correct_count += 1
            
        # Record Data to file
        this_exp.addData('wait_time', current_wait)
        this_exp.addData('stimulus', trial['label'])
        this_exp.addData('reaction_time', rt)
        this_exp.addData('is_correct', is_correct)
        this_exp.nextEntry()
        
        win.flip()
        core.wait(0.1)

# --- 6. Calculate and Display Final Stats ---
if total_trials > 0:
    avg_rt = np.mean(all_rts)
    acc_percent = (correct_count / total_trials) * 100
    
    final_text = (
        f"TIME'S UP!\n\n"
        f"Total Trials: {total_trials}\n"
        f"Correct Responses: {correct_count}\n"
        f"Accuracy: {acc_percent:.1f}%\n"
        f"Average RT: {avg_rt:.3f} seconds\n\n"
        f"Press any key to exit."
    )
else:
    final_text = "No trials completed.\nPress any key to exit."

summary_display = visual.TextStim(win, text=final_text, color="black", height=30)
summary_display.draw()
win.flip()
event.waitKeys()

win.close()
core.quit()