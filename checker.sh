
check_file_exists()
  if [ -f $1 ]
  then
    echo "$1 exists... OK!"
  else
    echo "ERROR: $1 does not exist"
    exit 1
  fi

bindir="pargenes/pargenes_binaries"

echo "Running checker.sh..."
if [[ "$OSTYPE" == "darwin"* ]]; then
  echo "Not checking .so files... OK"
else
  check_file_exists "$bindir/raxml-ng-mpi.so"
  check_file_exists "$bindir/modeltest-ng-mpi.so"
fi
check_file_exists "$bindir/raxml-ng"
check_file_exists "$bindir/modeltest-ng"
check_file_exists "$bindir/mpi-scheduler"
echo "End of checks... No error detected!"

