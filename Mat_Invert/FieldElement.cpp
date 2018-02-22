#include "FieldElement.h"




FieldElement::FieldElement(const unsigned long v)
{
	num_value = v;
	bits = std::bitset<32>(v);
}

FieldElement::FieldElement(const std::bitset<32> b)
{
	bits = b;
	num_value = bits.to_ulong();
}

int FieldElement::mostSignificantBit() const{
	int ret = 31;
	while (bits[ret] == 0) {
		ret--;
		if (ret == -1)
			return -1;
	}
	return ret;
}

FieldElement FieldElement::invert(const FieldElement & mod) const
{
	FieldElement temp = FieldElement(1);
	FieldElement one = FieldElement(1);
	int factor = 1;
	while (((temp*(*this)) % mod).num_value != 1) {
		factor++;
		temp = FieldElement(factor);
	}
	
	return FieldElement(factor);
}

FieldElement::~FieldElement()
{
}
