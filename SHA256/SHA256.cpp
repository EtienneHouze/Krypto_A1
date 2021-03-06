
#include <iostream>
#include <vector>
#include <bitset>
#include <string>

using namespace std;

using Word = unsigned long;


// Initialization of the various constants needed for the hash.
Word k_constants[64] = {
	0x428a2f98,
	0x71374491,
	0xb5c0fbcf,
	0xe9b5dba5,
	0x3956c25b,
	0x59f111f1,
	0x923f82a4,
	0xab1c5ed5,
	0xd807aa98,
	0x12835b01,
	0x243185be,
	0x550c7dc3,
	0x72be5d74,
	0x80deb1fe,
	0x9bdc06a7,
	0xc19bf174,
	0xe49b69c1,
	0xefbe4786,
	0x0fc19dc6,
	0x240ca1cc,
	0x2de92c6f,
	0x4a7484aa,
	0x5cb0a9dc,
	0x76f988da,
	0x983e5152,
	0xa831c66d,
	0xb00327c8,
	0xbf597fc7,
	0xc6e00bf3,
	0xd5a79147,
	0x06ca6351,
	0x14292967,
	0x27b70a85,
	0x2e1b2138,
	0x4d2c6dfc,
	0x53380d13,
	0x650a7354,
	0x766a0abb,
	0x81c2c92e,
	0x92722c85,
	0xa2bfe8a1,
	0xa81a664b,
	0xc24b8b70,
	0xc76c51a3,
	0xd192e819,
	0xd6990624,
	0xf40e3585,
	0x106aa070,
	0x19a4c116,
	0x1e376c08,
	0x2748774c,
	0x34b0bcb5,
	0x391c0cb3,
	0x4ed8aa4a,
	0x5b9cca4f,
	0x682e6ff3,
	0x748f82ee,
	0x78a5636f,
	0x84c87814,
	0x8cc70208,
	0x90befffa,
	0xa4506ceb,
	0xbef9a3f7,
	0xc67178f2,
};

Word h_init[8] = {
	0x6a09e667,
	0xBB67AE85,
	0x3C6EF372,
	0xA54FF53A,
	0x510E527F,
	0x9B05688C,
	0x1F83D9AB,
	0x5BE0CD19
};

// Conversion from a long long to an 8-byte long array
vector<unsigned char> ltoB(unsigned long long entry) {
	vector<unsigned char> ret(8);
	for (unsigned char i = 0; i < 8; i++) {
		ret[7 - i] = entry >> (8 * i);
	}
	return ret;
}
//Conversion from a long to a 32bit array
vector<unsigned char> itoB(unsigned long entry) {
	vector<unsigned char> ret(4);
	for (unsigned char i = 0; i < 4; i++) {
		ret[3 - i] = (entry >> (8 * i));
	}
	return ret;
}
// Conversion from a 4-byte long array to an unsigned long
Word BtoI(vector<unsigned char> w) {
	unsigned long mult = 1;
	unsigned long ret = 0;
	for (int i = 0; i < 4; i++) {
		ret += mult * w[3 - i];
		mult *= 256;
	}
	return ret;
}
// Rotation to the right
Word rotR(Word w, int k) {
	bitset<32> bits = bitset<32>(w);
	bool mem;
	while (k > 0) {
		mem = (bits[0] == 1);
		for (int c = 0; c < 31; c++) {
			bits[c] = bits[c + 1];
		}
		if (mem)
			bits[31] = 1;
		else
			bits[31] = 0;
		k--;
	}
	return bits.to_ulong();
}
// Method to preprocess the message into a 512-bit multiplier message
vector<Word> preprocess(vector<unsigned char> message) {
	unsigned long long l = message.size() * 8;
	vector<unsigned char> ret = message;
	int K = 0;
	while ((l + 1 + K + 64) % 512 != 0)
		K++;
	int bytesToAdd = (K + 1) / 8;
	ret.push_back(0x80);
	for (unsigned char c = 1; c < bytesToAdd; c++)
		ret.push_back(0x00);
	vector<unsigned char> lInBytes = ltoB(l);
	for (unsigned char c = 0; c < 8; c++) {
		ret.push_back(lInBytes[c]);
	}
	vector<Word> fin = vector<Word>();
	for (int c = 0; c < ret.size(); c += 4) {
		vector<unsigned char> temp(4);
		temp[0] = ret[c];
		temp[1] = ret[c+1];
		temp[2] = ret[c+2];
		temp[3] = ret[c+3];
		fin.push_back(BtoI(temp));
	}
	return fin;
}
// The following are the various bitwise functions used in the hash process
Word ch(Word x, Word y, Word z) {
	return ((x & y) ^ ((~x)&z));
}

Word maj(Word x, Word y, Word z) {
	return ((x&y) ^ (x&z) ^ (y&z));
}

Word S_0(Word x) {
	Word w1, w2, w3;
	w1 = rotR(x, 2);
	w2 = rotR(x, 13);
	w3 = rotR(x, 22);
	return (w1^w2^w3);
}

Word S_1(Word x) {
	Word w1, w2, w3;
	w1 = rotR(x, 6);
	w2 = rotR(x, 11);
	w3 = rotR(x, 25);
	return (w1^w2^w3);
}

Word s_0(Word x) {
	Word w1, w2, w3;
	w1 = rotR(x, 7);
	w2 = rotR(x, 18);
	w3 = x >> 3;
	return (w1^w2^w3);
}

Word s_1(Word x) {
	Word w1, w2, w3;
	w1 = rotR(x, 17);
	w2 = rotR(x, 19);
	w3 = x >> 10;
	return (w1^w2^w3);
}


// Declaration of the hash variables
Word h0, h1, h2, h3, h4, h5, h6, h7;
// Method to initialize those variable
void init() {
	h0 = h_init[0];
	h1 = h_init[1];
	h2 = h_init[2];
	h3 = h_init[3];
	h4 = h_init[4];
	h5 = h_init[5];
	h6 = h_init[6];
	h7 = h_init[7];
}
// Updates the hash variables for a chunk from the message
void processChunk(vector<Word> chunk) {
	vector<Word> words(64);
	for (unsigned char i = 0; i < 16; i++) {
		words[i] = chunk[i];
	}
	for (unsigned char i = 16; i < 64; i++) {
		words[i] = s_1(words[i - 2])
			+ words[i - 7]
			+ s_0(words[i - 15])
			+ words[i - 16];
	}

	Word a, b, c, d, e, f, g, h;
	a = h0;
	b = h1;
	c = h2;
	d = h3;
	e = h4;
	f = h5;
	g = h6;
	h = h7;

	for (unsigned char t = 0; t < 64; t++) {
		Word temp1 = h
			+ S_1(e)
			+ ch(e, f, g)
			+ k_constants[t]
			+ words[t];
		Word temp2 = S_0(a) + maj(a, b, c);
		h = g;
		g = f;
		f = e;
		e = d + temp1;
		d = c;
		c = b;
		b = a;
		a = temp1 + temp2;
	}

	h0 += a;
	h1 += b;
	h2 += c;
	h3 += d;
	h4 += e;
	h5 += f;
	h6 += g;
	h7 += h;
}
// Loops over the chunks to finally return the final digest as a concatenation of the hash variables.
vector<unsigned char> SHA256(vector<unsigned char> message) {
	vector<unsigned char> ret = vector<unsigned char>(32);
	vector<Word> mess_preproc = preprocess(message);
	init();
	for (int n = 0; n < mess_preproc.size(); n += 16) {
		vector<Word> chunk(16);
		for (unsigned char c = 0; c < 16; c++) {
			chunk[c] = mess_preproc[n+c];
		}
		processChunk(chunk);
	}
	vector<unsigned char> h0_vec = itoB(h0);
	vector<unsigned char> h1_vec = itoB(h1);
	vector<unsigned char> h2_vec = itoB(h2);
	vector<unsigned char> h3_vec = itoB(h3);
	vector<unsigned char> h4_vec = itoB(h4);
	vector<unsigned char> h5_vec = itoB(h5);
	vector<unsigned char> h6_vec = itoB(h6);
	vector<unsigned char> h7_vec = itoB(h7);
	for (unsigned char c = 0; c < 4; c++) {
		ret[c] = h0_vec[c];
		ret[4+c] = h1_vec[c];
		ret[8+c] = h2_vec[c];
		ret[12+c] = h3_vec[c];
		ret[16+c] = h4_vec[c];
		ret[20+c] = h5_vec[c];
		ret[24+c] = h6_vec[c];
		ret[28+c] = h7_vec[c];
	}
	return ret;
}

int main()
{

	string line = string();
	int t = 0;
	while (getline(cin,line,'\n')) {	// Loop over the lines
		// Convert the string to a vector of bytes.
		vector<unsigned char> buffer;
		for (int pos = 0; pos < line.size(); pos +=2) {
			string sub = line.substr(pos, 2);
			unsigned char temp = strtoul(sub.c_str(), nullptr, 16);
			buffer.push_back(temp);
		}
		// Computation of the hash and printing of the result.
		vector<unsigned char> mess_out = SHA256(buffer);
		for (unsigned char i = 0; i < 32; i++)
			cout << noskipws << hex << (int)mess_out[i];
		cout << endl;

	}
	//char temp;
	//while (cin >> noskipws >>temp) {
	//	if (temp != '\n') {
	//		cout << "helle" << endl;
	//		line.push_back(temp);
	//	}
	//	else {
	//		vector<unsigned char> buffer;
	//		for (int pos = 0; pos < line.size(); pos +=2) {
	//			string sub = line.substr(pos, 2);
	//			unsigned char temp = strtoul(sub.c_str(), nullptr, 16);
	//			buffer.push_back(temp);
	//		}
	//		// Computation of the hash and printing of the result.
	//		vector<unsigned char> mess_out = SHA256(buffer);
	//		for (unsigned char i = 0; i < 32; i++)
	//			cout << noskipws << hex << (int)mess_out[i];
	//		cout << endl;
	//		line = string();
	//	}
	//}

	return 0;
}