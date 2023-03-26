#include <bits/stdc++.h>
using namespace std;

#define M 16

int main() {
  ifstream file("san.txt");
  unordered_map<string,tuple<int,vector<string>>> data2;
  vector<string> strings;
  string line;
  while (getline(file,line)) {
    stringstream lineStream(line);
    int n;
    string s;
    lineStream >> s >> n;
    string s2;
    vector<string> lineData;
    while (lineStream >> s2) {
      lineData.push_back(s2);
    }
    data2[s] = make_tuple(n, lineData);
    strings.push_back(s);
  }
  unordered_map<string,tuple<int,vector<int>>> data;
  for (auto x : data2) {
    vector<int> v;
    for (auto s : get<1>(x.second)) {
      for (int i = 0; i < strings.size(); ++i) {
        if (strings[i] == s) {
          v.push_back(i);
        }
      }
    }
    data[x.first] = make_tuple(get<0>(x.second),v);
  }

  vector<int> real;
  set<int> rset;
  for (int x = 0; x < strings.size(); ++x) {
    if (get<0>(data[strings[x]]) > 0) {
      real.push_back(x);
      rset.insert(x);
    }
  }

  unordered_map<int,int> stor;
  for (int i = 0; i < real.size(); ++i) {
    stor[real[i]] = i;
  }

  unordered_map<int,int> vals;
  for (int i = 0; i < (1<<real.size()); ++i) {
    int val = 0;
    for (int j = 0; j < real.size(); ++j) {
      if ((1<<j)&i) {
        val += get<0>(data[strings[real[j]]]);
      }
    }
    vals[i] = val;
  }


  map<tuple<int,int,int>,unsigned>y;
  int sp = 0;
  for (int x = 0; x < strings.size(); ++x) {
    cout << "init phase " << sp << endl;
    ++sp;
    for (int z = 0; z < strings.size(); ++z) {
      for (int i = 0; i < (1<<real.size()); ++i) {
        y[make_tuple(x, z, i)] = 0;
      }
    }
  }
  for (int j = 1; j <= 26; ++j) {
    cout << "round " << j << endl;
    for (int x = 0; x < strings.size(); ++ x) {
      cout << "    shift phase " << x << endl;
      for (int z = 0; z < strings.size(); ++z) {
        for (int i = 0; i < (1<<real.size()); ++i) {
          y[make_tuple(x, z, i)] <<= M;
        }
      }
    }
    for (int x = 0; x < strings.size(); ++x) {
      cout << "    subround " << x << endl;
      for (int z = 0; z < strings.size(); ++z) {
        for (int i = 0; i < (1<<real.size()); ++i) {
          unsigned w = 0;
          for (auto d : get<1>(data[strings[x]])) {
            for (auto d2 : get<1>(data[strings[z]])) {
              w = max(w, (y[make_tuple(d, d2, i)]>>M)%(1<<M) + vals[i]);
            }
            if (rset.count(z) && !((1<<stor[z])&i)) {
              w = max(w, (y[make_tuple(d, z, i|(1<<stor[z]))]>>M)%(1<<M) + vals[i]);
            }
          }
          if (rset.count(x) && !((1<<stor[x])&i)) {
            for (auto d2 : get<1>(data[strings[z]])) {
              w = max(w, (y[make_tuple(x, d2, i|(1<<stor[x]))]>>M)%(1<<M) + vals[i]);
            }
            if (rset.count(z) && !((1<<stor[z])&i)) {
              w = max(w, (y[make_tuple(x, z, i|(1<<stor[x])|(1<<stor[z]))]>>M)%(1<<M) + vals[i]);
            }
          }
          y[make_tuple(x, z, i)] = y[make_tuple(x, z, i)] + w;
        }
      }
    }
  }
  int si;
  for (si = 0; si < strings.size(); ++si) {
    if (strings[si] == "AA") {
      break;
    }
  }
  cout << y[make_tuple(si, si, 0)]%(1<<M) << endl;
}
