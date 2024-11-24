ffmpeg -loop 1 -i BOY_0ac80cdaea57d5b64ea14fa02ef31dcb.jpg -r 1 -c:v libx264 -t 5 -pix_fmt yuv420p BOY_0ac80cdaea57d5b64ea14fa02ef31dcb.mp4

@REM foreach all jpg files in the current directory and echo the file name
for %%i in (*.jpg) do (
    echo %%i
    @REM ffmpeg -loop 1 -i %%i -c:v libx264 -t 5 -pix_fmt yuv420p %%~ni.mp4
    ffmpeg -loop 1 -i %%i -r 5 -c:v libx264 -t 5 -pix_fmt yuv420p %%~ni.mp4
)

@REM foreach all jpg files in image_list.txt and echo the file name
@REM for /f "tokens=*" %%i in (image_list.txt) do (
@REM     echo %%i
@REM     ffmpeg -loop 1 -i %%i -c:v libx264 -t 5 -pix_fmt yuv420p %%~ni.mp4
@REM     ffmpeg -loop 1 -i %%i -r 1 -c:v libx264 -t 5 -pix_fmt yuv420p %%~ni.mp4
@REM )
