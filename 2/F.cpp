#include <iostream>
#include <vector>

using namespace std;

bool good (int cnt, int q, int s, int t){
	return (t/q+t/s>=cnt);
}

main(){
	int n, quick, slow, m;
	
	cin >> n;
	cin >> quick;
	cin >> slow;
	
	if (quick>slow){
		int buf;
		buf=quick;
		quick=slow;
		slow=buf;
	}
	
	int l=0;
	int r=(n-1)*slow;
	
	while(r-l>1){
		m=(l+r)/2;
		if (!good(n-1,quick,slow,m)){
			l=m;
		}
		else{
			r=m;
		}
	}
	
	cout << r+quick;
}
