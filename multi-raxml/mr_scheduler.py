import sys
import subprocess
import os
import mr_commons

def get_mpi_scheduler_exec():
  repo_root = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
  return os.path.join(repo_root, "mpi-scheduler", "build", "mpi-scheduler")

def run_mpi_scheduler(library, scheduler, commands_filename, output_dir, ranks):
  
  sys.stdout.flush()
  command = []
  command.append("mpirun")
  command.append("-np")
  command.append(str(ranks))
  command.append(get_mpi_scheduler_exec())
  if (scheduler == "onecore"):
    command.append("--onecore-scheduler")
  else:
    command.append("--split-scheduler")
  command.append(library)
  command.append(commands_filename)
  command.append(output_dir)
  
  logs_file = mr_commons.get_log_file(output_dir, "logs")
  out = open(logs_file, "w")
  print("Calling mpi-scheduler: " + " ".join(command))
  print("Logs will be redirected to " + logs_file)
  p = subprocess.Popen(command, stdout=out, stderr=out)
  p.wait()
