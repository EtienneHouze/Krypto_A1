#include <vector>
#include <iostream>
#include <bitset>

#include "FieldElement.h"

using namespace std;


const FieldElement MODULO = FieldElement(17);


//Elem Euclidean_r(Elem p, Elem q) {
//	while (p >= q) {
//		int q_bis = q;
//		while ((q_bis<<1) < p)
//			q_bis = q_bis << 1;
//		p = p ^ q_bis;
//	}
//	return p;
//}

vector<vector<FieldElement>> GaussInvert(const vector<vector<FieldElement>>& mat) {
	//TODO : finish Gauss Pivot
	vector<vector<FieldElement>> matCopy = mat;
	vector<vector<FieldElement>> ret = vector<vector<FieldElement>>(matCopy.size(), vector<FieldElement>(matCopy.size(), FieldElement(0)));
	for (int c = 0; c < ret.size(); c++) {
		ret[c][c] = FieldElement(1);
	}
	for (int row = 0; row < ret.size(); row++) {

		// The following block finds the maximum and swaps lines
		int k = row;
		unsigned long max_pivot = 0;
		for (int i = row; i < ret.size(); i++) {
			if (matCopy[i][row].num_value > max_pivot/* && matCopy[i][row].num_value != 3*/) {
				k = i;
				max_pivot = matCopy[i][row].num_value;
			}
		}
		vector<FieldElement> tempRow = matCopy[row];
		matCopy[row] = matCopy[k];
		matCopy[k] = tempRow;
		tempRow = ret[row];
		ret[row] = ret[k];
		ret[k] = tempRow;
		//We then operate over the rows (removing them)
		vector<FieldElement> rowToRemove = matCopy[row];
		vector<FieldElement> rowToRemoveRet = ret[row];
		FieldElement mult = matCopy[row][row].invert(256 + 16 + 8 + 2 + 1)%MODULO;
		for (int c = 0; c < rowToRemove.size(); c++) {
			rowToRemove[c] = (rowToRemove[c] * mult) % MODULO;
			rowToRemoveRet[c] = (rowToRemoveRet[c] * mult) % MODULO;
		}
		for (int r = 0; r < ret.size(); r++) {
			if (r == row)
				for (unsigned char c = 0; c < ret.size(); c++) {
					matCopy[r][c] = (matCopy[r][c] * mult)%MODULO;
					ret[r][c] = (ret[r][c] * mult) % MODULO;
				}
			else {
				for (unsigned char c = 0; c < ret.size(); c++) {
					FieldElement coeffLine = matCopy[r][row];
					matCopy[r][c] = matCopy[r][c] + ((matCopy[r][row] * rowToRemove[c]) % MODULO);
					ret[r][c] = ret[r][c] + ((coeffLine * rowToRemoveRet[c]) % MODULO);
				}
			}
		}
	}
	return ret;
}



int main(int argc, char* argv[]) {
	FieldElement e1 = FieldElement(0x01);
	FieldElement e2 = FieldElement(0x02);
	FieldElement e3 = FieldElement(0x03);
	//Elem ret = Euclidean_r(e1, e2);
	vector<vector<FieldElement>> matrix = vector<vector<FieldElement>>(4, vector<FieldElement>(4));
	matrix[0][0] = e2;
	matrix[0][1] = e3;
	matrix[0][2] = e1;
	matrix[0][3] = e1;
	matrix[1][0] = e1;
	matrix[1][1] = e2;
	matrix[1][2] = e3;
	matrix[1][3] = e1;
	matrix[2][0] = e1;
	matrix[2][1] = e1;
	matrix[2][2] = e2;
	matrix[2][3] = e3;
	matrix[3][0] = e3;
	matrix[3][1] = e1;
	matrix[3][2] = e1;
	matrix[3][3] = e2;
	vector<vector<FieldElement>> test_out = GaussInvert(matrix);
	FieldElement test = e2.invert(FieldElement(256+16+8+2+1));
	//cout << Euclidean_r(e1,e2) << endl;
	return 0;
}