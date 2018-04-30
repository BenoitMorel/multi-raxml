import os
import mr_commons

def build_modeltest_command(msas, output_dir, ranks): 
  modeltest_commands_file = os.path.join(output_dir, "modeltest_command.txt")
  modeltest_run_output_dir = os.path.join(output_dir, "modeltest_run")
  modeltest_results = os.path.join(modeltest_run_output_dir, "results")
  mr_commons.makedirs(modeltest_results)
  with open(modeltest_commands_file, "w") as writer:
    for name, msa in msas.items():
      if (not msa.valid):
        continue
      modeltest_fasta_output_dir = os.path.join(modeltest_results, name)
      mr_commons.makedirs(modeltest_fasta_output_dir)
      writer.write("modeltest_" + name + " ") 
      writer.write("32 " + str(msa.taxa * msa.sites)) #todobenoit smarter ordering
      writer.write(" -i ")
      writer.write(msa.path)
      writer.write(" -t mp ")
      writer.write(" -o " +  os.path.join(modeltest_results, name, name))
      writer.write(" " + msa.modeltest_arguments + " ")
      writer.write("\n")
  return modeltest_commands_file

def parse_modeltest_results(modeltest_criteria, msas, output_dir):
  modeltest_run_output_dir = os.path.join(output_dir, "modeltest_run")
  modeltest_results = os.path.join(modeltest_run_output_dir, "results")
  models = {}
  for name, msa in msas.items():
    if (not msa.valid):
      continue
    modeltest_outfile = os.path.join(modeltest_results, name, name + ".out")  
    with open(modeltest_outfile) as reader:
      read_next_model = False
      for line in reader.readlines():
        if (line.startswith("Best model according to " + modeltest_criteria)):
            read_next_model = True
        if (read_next_model and line.startswith("Model")):
          model = line.split(" ")[-1][:-1]
          msa.set_model(model)
          if (not model in models):
            models[model] = 0
          models[model] += 1
          break
  # write a summary of the models
  with open(os.path.join(modeltest_run_output_dir, "summary.txt"), "w") as writer:
    for model, count in sorted(models.items(), key=lambda x: x[1], reverse=True):
      writer.write(model + " " + str(count) + "\n")


