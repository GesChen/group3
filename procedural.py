import os 
from pathlib import Path

path = "videos"
videos = [str(file) for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))]

output = ""
for v in videos:
    basename = Path(v).stem
    
    output += f'''
<div class="icon">
    <video src="videos/{basename}.mp4" id="{basename}" class="video" loop autoplay muted></video>
    <div>
        <input type="checkbox" id="cb{basename}">
        <label for="cb{basename}">unmute</label>
    </div>
</div>
'''
    
print(output)