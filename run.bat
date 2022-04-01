set loopcount=3
:loop
start "" python main.py https://hub.hkusthub.link/qapEc48/unusual-petty-venture
set /a loopcount=loopcount-1
if %loopcount%==0 goto exitloop
goto loop
:exitloop
