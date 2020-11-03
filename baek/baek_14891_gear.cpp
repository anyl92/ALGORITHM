#include <iostream>
#include <vector>
using namespace std;

int gears[6], K, xor_list[3];

void init() {
	freopen("./input.txt", "r", stdin);
	// vector<char> bits[9];
	char bits[9];

	for (int i = 1; i <= 4; i++) {
		cin >> bits;
		for (int j = 0; j < 8; j++) {
			// cout << bits[li] << " ";
			gears[i] <<= 1;
			gears[i] |= (bits[j] - '0');
		}
	}

	//for (int li = 0; li < 5; li++) {
	//	printf("%d \n", gears[li]);
	//}
	cin >> K;
}

void turn(int n, int d) {
	if (d > 0) {
		gears[n] = (gears[n] | ((gears[n] & 1) << 8)) >> 1;
	}
	else {
		gears[n] = ((gears[n] << 1) | ((gears[n] >> 7) & ~(1 << 8)));
	}

}

int set_j(int i, int dir, int chk) {
	if (i % 2 != chk) {
		return dir * -1;
	}
	else {
		return dir;
	}

}

void spread(int i, int d, int c, int flag) {
	while (0 <= i < 3) {
		if (!xor_list[i]) {
			break;
		}
		if (flag) {
			i += 1;
		}

		int j = set_j(i, d, c);
		turn(i, j);

		if (flag == -1) {
			i -= 1;
		}
	}
}

int sol() {
	int res = 0, num, dir, chk;

	while (K--) {
		for (int i = 0; i < 3; i++) {
			xor_list[i] = bool(gears[i] & (1 << 5)) ^ bool(gears[i+1] & (1 << 1));
		}
		//for (int li = 0; li < 3; li++) {
		//	printf("%d \n", xor_list[li]);
		//}

		cin >> num >> dir;
		num -= 1;
		chk = num % 2;

		turn(num, dir);
		spread(num - 1, dir, chk, -1);
		spread(num, dir, chk, 1);
	}

	for (int i = 0; i < 4; i++) {
		int tmp = 0;
		if (gears[i] & ((1 << 7) == (1 << 7))) {
			tmp = 1;
			for (int j = 0; j < i; j++) {
				tmp *= 2;
				//res += 2 ** i;
			}
			res += tmp;
		}
	}
	printf("%d", res);
	return res;
}

void main() {
	init();
	sol();
}