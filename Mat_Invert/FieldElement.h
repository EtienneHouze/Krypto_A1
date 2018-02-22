#pragma once
#include <bitset>

class FieldElement
{
public:

	unsigned long num_value;
	std::bitset<32> bits;

public:
	FieldElement() {
		num_value = 0;
		bits = std::bitset<32>();
	};

	FieldElement(const unsigned long v);

	FieldElement(const std::bitset<32> b);

	int mostSignificantBit() const;

	FieldElement operator+(const FieldElement& other)const {
		FieldElement ret = FieldElement();
		for (unsigned char c = 0; c < 32; c++)
			ret.bits[c] = bits[c] ^ other.bits[c];
		ret.num_value = ret.bits.to_ulong();
		return ret;
	}

	FieldElement operator%(const FieldElement& other)const {
		FieldElement ret = FieldElement(num_value);
		while (ret.mostSignificantBit() >= other.mostSignificantBit()) {
			FieldElement new_other = FieldElement(other.num_value);
			while (new_other.mostSignificantBit() < ret.mostSignificantBit()){
				new_other = FieldElement(new_other.num_value * 2);
			}
			ret = new_other + ret;
		}
		return ret;
	}
	
	FieldElement invert(const FieldElement& mod)const;

	FieldElement operator*(const FieldElement& other) const {
		FieldElement ret = FieldElement(0);
		FieldElement temp = FieldElement(this->num_value);
		for (int c = 0; c <= other.mostSignificantBit(); c++) {
			if (other.bits[c] == 1)
				ret = ret + temp;
			temp = FieldElement(temp.num_value * 2);
		}
		return ret;
	}

	~FieldElement();
};

