@echo off
rem START or STOP Services
rem ----------------------------------
rem Check if argument is STOP or START

if not ""%1"" == ""START"" goto stop

if exist D:\campus-trade-test\xampp\hypersonic\scripts\ctl.bat (start /MIN /B D:\campus-trade-test\xampp\server\hsql-sample-database\scripts\ctl.bat START)
if exist D:\campus-trade-test\xampp\ingres\scripts\ctl.bat (start /MIN /B D:\campus-trade-test\xampp\ingres\scripts\ctl.bat START)
if exist D:\campus-trade-test\xampp\mysql\scripts\ctl.bat (start /MIN /B D:\campus-trade-test\xampp\mysql\scripts\ctl.bat START)
if exist D:\campus-trade-test\xampp\postgresql\scripts\ctl.bat (start /MIN /B D:\campus-trade-test\xampp\postgresql\scripts\ctl.bat START)
if exist D:\campus-trade-test\xampp\apache\scripts\ctl.bat (start /MIN /B D:\campus-trade-test\xampp\apache\scripts\ctl.bat START)
if exist D:\campus-trade-test\xampp\openoffice\scripts\ctl.bat (start /MIN /B D:\campus-trade-test\xampp\openoffice\scripts\ctl.bat START)
if exist D:\campus-trade-test\xampp\apache-tomcat\scripts\ctl.bat (start /MIN /B D:\campus-trade-test\xampp\apache-tomcat\scripts\ctl.bat START)
if exist D:\campus-trade-test\xampp\resin\scripts\ctl.bat (start /MIN /B D:\campus-trade-test\xampp\resin\scripts\ctl.bat START)
if exist D:\campus-trade-test\xampp\jetty\scripts\ctl.bat (start /MIN /B D:\campus-trade-test\xampp\jetty\scripts\ctl.bat START)
if exist D:\campus-trade-test\xampp\subversion\scripts\ctl.bat (start /MIN /B D:\campus-trade-test\xampp\subversion\scripts\ctl.bat START)
rem RUBY_APPLICATION_START
if exist D:\campus-trade-test\xampp\lucene\scripts\ctl.bat (start /MIN /B D:\campus-trade-test\xampp\lucene\scripts\ctl.bat START)
if exist D:\campus-trade-test\xampp\third_application\scripts\ctl.bat (start /MIN /B D:\campus-trade-test\xampp\third_application\scripts\ctl.bat START)
goto end

:stop
echo "Stopping services ..."
if exist D:\campus-trade-test\xampp\third_application\scripts\ctl.bat (start /MIN /B D:\campus-trade-test\xampp\third_application\scripts\ctl.bat STOP)
if exist D:\campus-trade-test\xampp\lucene\scripts\ctl.bat (start /MIN /B D:\campus-trade-test\xampp\lucene\scripts\ctl.bat STOP)
rem RUBY_APPLICATION_STOP
if exist D:\campus-trade-test\xampp\subversion\scripts\ctl.bat (start /MIN /B D:\campus-trade-test\xampp\subversion\scripts\ctl.bat STOP)
if exist D:\campus-trade-test\xampp\jetty\scripts\ctl.bat (start /MIN /B D:\campus-trade-test\xampp\jetty\scripts\ctl.bat STOP)
if exist D:\campus-trade-test\xampp\hypersonic\scripts\ctl.bat (start /MIN /B D:\campus-trade-test\xampp\server\hsql-sample-database\scripts\ctl.bat STOP)
if exist D:\campus-trade-test\xampp\resin\scripts\ctl.bat (start /MIN /B D:\campus-trade-test\xampp\resin\scripts\ctl.bat STOP)
if exist D:\campus-trade-test\xampp\apache-tomcat\scripts\ctl.bat (start /MIN /B /WAIT D:\campus-trade-test\xampp\apache-tomcat\scripts\ctl.bat STOP)
if exist D:\campus-trade-test\xampp\openoffice\scripts\ctl.bat (start /MIN /B D:\campus-trade-test\xampp\openoffice\scripts\ctl.bat STOP)
if exist D:\campus-trade-test\xampp\apache\scripts\ctl.bat (start /MIN /B D:\campus-trade-test\xampp\apache\scripts\ctl.bat STOP)
if exist D:\campus-trade-test\xampp\ingres\scripts\ctl.bat (start /MIN /B D:\campus-trade-test\xampp\ingres\scripts\ctl.bat STOP)
if exist D:\campus-trade-test\xampp\mysql\scripts\ctl.bat (start /MIN /B D:\campus-trade-test\xampp\mysql\scripts\ctl.bat STOP)
if exist D:\campus-trade-test\xampp\postgresql\scripts\ctl.bat (start /MIN /B D:\campus-trade-test\xampp\postgresql\scripts\ctl.bat STOP)

:end

