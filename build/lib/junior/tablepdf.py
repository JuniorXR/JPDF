from fpdf import FPDF
import os
from sympy import sympify
import json

class TablePDF(FPDF):
	def __init__(self,orientationvar=None):
		if orientationvar:
			super().__init__(unit="pt",orientation=orientationvar)
		else:
			super().__init__(unit="pt")

	def add_table(self, heading_row, data_rows, text_align="CENTER"):
		self.add_page()
		self.set_font("helvetica", size=12)

		# Dynamically generate col_widths based on the maximum number of columns
		max_cols = max(len(heading_row), *[len(row) for row in data_rows])
		col_width = tuple([120] * max_cols)  # Default width, adjust as needed

		with self.table(col_widths=col_width, text_align=text_align) as table:
			# Add heading row
			heading_row_cells = table.row()
			for datum in heading_row:
				heading_row_cells.cell(datum)  # Adjust width based on col_widths

			# Add data rows
			for data_row in data_rows:
				row = table.row()
				for datum in data_row:
					# Check if the datum starts with '!' for evaluation
					if datum.startswith('!'):
						result = self.evaluate_expression(datum[1:])
						row.cell(str(result))  # Adjust width based on col_widths
					else:
						row.cell(datum)  # Adjust width based on col_widths

	def evaluate_expression(self, expression):
		try:
			result = sympify(expression)
			return result
		except Exception as e:
			print(f"Error evaluating expression '{expression}': {e}")
			return None

	def create_pdf_from_file(self, output_file_name):
		file_name = output_file_name + '.txt'
		file_path = os.path.join(os.getcwd(), file_name)
		print(f"Log: file_path - {file_path}")
		try:
			with open(file_path, 'r') as file:
				lines = file.readlines()
				heading_row = []
				data_rows = []
				print(lines)

				for line in lines:
					line = line.strip()
					print(line)
					if line.startswith('head:'):
						headings_line = line[len('head:'):].strip()
						heading_row = headings_line.split(',')
					elif line.startswith('body:'):
						body_line = line[len('body:'):].strip()
						data_rows.append(body_line.split(','))
				print("file hasbeen readed!")
			
				if heading_row and data_rows:
            # Call add_table with parsed data
					self.add_table(heading_row, data_rows)
					pdf_output_path = f"{output_file_name}.pdf"
					self.output(pdf_output_path)
					print(f"PDF created successfully: {pdf_output_path}")
				else:
					print("heads:",heading_row,"\nbodys:",data_rows)
		except Exception as e:
			print(f"Error: {e}")




#This Class will be used to make contents for the tablePDF class 
class TableContentParser:
	#on initialisation give a name that will be output file then make a list of keys and values and put them in the perser then close the perser
	def __init__(self,content_name=None):
		if content_name:
			try:
				self.defaultTableContentFile=open(content_name+".txt","a+")
				
			except FileNotFoundError:
				self.defaultTableContentFile=open("table_contents.txt","a+")
		self.keys=[]
		self.values=[]
		self.contents={}
	def getContentFilePath(self):
		return self.defaultTableContentFile.name

	def __putKeys(self,keys:list):
		self.keys=keys
	def __putValues(self,values:list):
		self.values=values
		
	def putKeysAndValues(self,keys:list,vals:list):
		self.__putKeys(keys)
		self.__putValues(vals)
		self.contents=self.__merge()

	def __merge(self):
	#this private func will be auto called after the putKeysAndValues() fucntion runs
	#this function merges the keys and values as a python dict object and returns them into the class variable contents
		return dict(zip(self.keys,self.values))


	def parse(self):
		try:
			if self.keys:
				self.defaultTableContentFile.write("head:")
				self.defaultTableContentFile.write(','.join(self.keys))
				self.defaultTableContentFile.write("\n")
			
			if self.values:
				num_columns = len(self.keys)
				for index, item in enumerate(self.values):
					if index % num_columns == 0:
						self.defaultTableContentFile.write("body:")
					self.defaultTableContentFile.write(item)
					if (index + 1) % num_columns != 0:
						self.defaultTableContentFile.write(',')
					else:
						self.defaultTableContentFile.write('\n')
			self.closeParser()
		except Exception as e:
			return f"Error in creating content file or the final output file: {e}"
		return "Content Created Successfully!"


	def closeParser(self):
		#This func has to be called before code runs
		self.defaultTableContentFile.close()

# Example usage:
class Runner:
	'''Call this class to make pdf file from the Content file
E.g. - Runner().run()
'run()' function takes the file name which will be created and it will be the name of pdf file. If no value is given is the 'run() function' then it will ask in the runtime, so be careful of that!
'''
	def run(self,name=None,orientation=None):
		pdf = TablePDF()
		if orientation:
			pdf = TablePDF(orientationvar=orientation)
		if name:
			pdf.create_pdf_from_file(name)
		else:
			name=input("enter file name:")
			pdf.create_pdf_from_file(name)