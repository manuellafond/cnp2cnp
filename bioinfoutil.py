import random
import sys
import argparse
import os
from subprocess import Popen, PIPE
from shutil import copyfile
import subprocess
import math


class BioinfoUtil:

	@staticmethod
	def write_matrix_to_phylip(outfile, names, matrix):
		strout = str(len(matrix)) + "\n"

		for i in range(len(matrix)):
			strout += names[i].ljust(10) + " "
			for j in range(len(matrix[i])):
				if j != 0:
					strout += " "
				strout += str(matrix[i][j])
			strout += "\n"
		f = open(outfile, 'w')
		f.write(strout)
		f.close()

	@staticmethod
	def get_rf_dist(treefile1, treefile2):
		proc = subprocess.Popen(["python rfdist.py " + treefile1 + " " + treefile2], stdout=subprocess.PIPE, shell=True)
		(out, err) = proc.communicate()
		
		pz = out.split("/")
		return [int(pz[0]), int(pz[1])]


	@staticmethod
	def run_phylip_nj(distfile, outfile):

		if os.path.exists("infile"):
  			os.remove("infile")
		if os.path.exists("outfile"):
  			os.remove("outfile")
		if os.path.exists("outtree"):
  			os.remove("outtree")

		copyfile(distfile, "infile")

		pr = Popen(['phylip', 'neighbor'], stdout=PIPE, stderr=PIPE, stdin=PIPE)

		pr.stdin.write("y\n")

		pr.wait()

		copyfile("outtree", outfile)

		#pr.stdin.write(distfile + "\n")

        ## say yes


		#cmd = "phylip neighbor -datafile " + distfile + " -outfile " + outfile
		#os.system(cmd)
