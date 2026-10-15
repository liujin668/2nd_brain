# Source this file while the current directory is the extracted template root.
# This is a path convenience only; it does not initialize vendor tools or licenses.
if [ -f ./script/socflow.py ] && [ -f ./config/profiles.json ]; then
    SOC_UVM_ROOT="$(pwd -P)"
    export SOC_UVM_ROOT
    printf '%s\n' "SOC_UVM_ROOT=$SOC_UVM_ROOT" 'Use your approved site setup for VCS/Xcelium, UVM, VIP and LSF.'
else
    printf '%s\n' 'First cd to the template root, then run: . ./env_setup.sh' >&2
fi
