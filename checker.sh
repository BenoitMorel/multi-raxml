
check_file_exists()
  if [ -f $1 ]
  then
    echo "$1 exists... OK!"
  else
    echo "ERROR: $1 does not exist"
    exit 1
  fi

if [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then
  check_file_exists "raxml-ng/bin/raxml-ng-mpi.so"
  check_file_exists "modeltest/build/src/modeltest-ng-mpi.so"
fi
check_file_exists "raxml-ng/bin/raxml-ng"
check_file_exists "modeltest/bin/modeltest-ng"
check_file_exists "MPIScheduler/build/mpi-scheduler"
echo "End of checks... No error detected!"

