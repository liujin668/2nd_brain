# Source this file while the current directory is the extracted template root.
# This does not initialize vendor tools or licenses and does not modify PATH.
if ( -f ./script/socflow.py && -f ./config/profiles.json ) then
    setenv SOC_UVM_ROOT "$cwd"
    echo "SOC_UVM_ROOT=$SOC_UVM_ROOT"
    echo "Use your approved site setup for VCS/Xcelium, UVM, VIP and LSF."
else
    echo "First cd to the template root, then run: source ./env_setup.csh"
endif
