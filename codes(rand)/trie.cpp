#include <bits/stdc++.h>
#include <fstream>
using namespace std;

typedef struct TrieNode
{
  TrieNode* child[26];
  bool isEnd;
}TrieNode;
typedef TrieNode* pTn;
class Trie{
  public:
    Trie();
    ~Trie();
    void insert(string);
    bool search(string);
    void remove(string);
    vector<string> top_n_suf(string); 
  private:
    void top_n_sufR(vector<pair<string,int>>&,pair<string,int>&,pTn,int,int);
    void clear(pTn);
    int min_sort(pair<string,int>&,vector<pair<string,int>>&);
    pTn removeR(string,pTn,int);
    bool nochild(pTn);
    char getchar(int);
    int getidx(char);
    pTn root=NULL;
    pTn getnode();
};

pTn Trie::getnode(){
  pTn new_node = new TrieNode();
  for(int i=0;i<26;i++) new_node->child[i] = NULL;
  return new_node;
}

char Trie::getchar(int x){return ('a'+x);}
int Trie::getidx(char x){return x-'a';}

bool Trie::nochild(pTn node){
  for (int i=0;i<26;i++){
    if (node->child[i]) return false;
  }
  return true;
}

Trie::Trie(){
  this->root = getnode();
}

Trie::~Trie(){
  clear(this->root);
}

void Trie::clear(pTn node){
  for (int i=0;i<26;i++){
    if (node->child[i]){
      clear(node->child[i]);
    }
  }
  delete node;
}

void Trie::insert(string key){
  pTn temp = this->root;
  int n = key.length(),i,idx;
  for (i = 0;i<n;i++){
    idx = getidx(key[i]);
    if (!temp->child[idx]) temp->child[idx] = getnode();
    temp = temp->child[idx];
  }
  temp->isEnd = true;
}

pTn Trie::removeR(string key,pTn node,int i){
  if (!node) return NULL;
  if (key.length() == i) node->isEnd = false;
  else {
    int idx = getidx(key[i]);
    node->child[idx] = removeR(key, node->child[idx],i+1);
  }
  if (!node->isEnd && nochild(node)){
    delete node;
    node = NULL;
  }
  return node;
}

void Trie::remove(string key){
  this->root = removeR(key,this->root,0);
}

bool Trie::search(string key){
  pTn temp = this->root;
  int n = key.length(),i,idx;
  for (i=0;i<n;i++){
    idx = getidx(key[i]);
    if (!temp->child[idx]) return false;
    temp=temp->child[idx];
  }
  return temp->isEnd;
}

int Trie::min_sort(pair<string,int> &p, vector<pair<string,int>>& arr){
  int n = arr.size();
  bool within = false;
  for (int i=0;i<n;i++){
    if (p.second < arr[i].second){
      for (int j=n-1;j>i;j--){
        arr[j].first = arr[j-1].first;arr[j].second = arr[j-1].second;
      }
      arr[i].first = p.first; arr[i].second = p.second;
      within = true;
      break;
    }
  }
  if (!within){arr.push_back(pair<string,int>(p.first,p.second));n++;};
  return (n>=3)? arr[n-1].second: INT_MAX; 
}

void Trie::top_n_sufR(vector<pair<string,int>>& top_n,pair<string,int>& p,pTn node,int d,int maxd){
  if (d>=maxd) return;
  string pre = p.first;
  for (int i=0;i<26;i++){
    if (node->child[i]){
      p.first = pre+getchar(i);
      p.second =d;
      if (node->child[i]->isEnd) maxd = min_sort(p,top_n);
      top_n_sufR(top_n,p,node->child[i],d+1,maxd); 
    }
  } 
}

vector<string> Trie::top_n_suf(string key){
  int n = key.length(),idx;
  pTn temp = this->root;
  vector<string> out; 
  for (int i=0;i<n;i++){
    idx = getidx(key[i]);
    if (!temp->child[idx]){return out;}
    temp = temp->child[idx];
  }
  vector<pair<string,int>> top_n;
  pair<string,int> p = {"",0};
  top_n_sufR(top_n,p,temp,1,INT_MAX);
  
  for (int i=0;i<top_n.size();i++)
    out.push_back(top_n[i].first);
  return out;
}       


int main(){
  Trie auto_cmplt;
  ifstream fin;
  fin.open("./common_words.txt");
  string word;
  while (fin){
    getline(fin,word);
    auto_cmplt.insert(word);
  }
  fin.close();
  word = "";
  char res = ' ';
  while (res != 'q'){
    cout << "PREV:-\n WORD: " << word<<" TASK: "<<res<<endl<<endl;
    cout << "ENTER: ";
    cin >> word;
    cout << "TASK(c/f/d/s): ";
    cin >> res;
    if (res=='c'){
      vector<string> sug = auto_cmplt.top_n_suf(word);
      for (int i =0;i<sug.size();i++){
        cout<<i<<")"<<word+sug[i] << " ";
      }
      cout << endl;
    } else if (res == 'f'){
      if (!auto_cmplt.search(word)) auto_cmplt.insert(word);
    } else if (res == 'd'){
      auto_cmplt.remove(word);
    } else if (res == 's'){
      if (auto_cmplt.search(word)) cout << "available!"<<endl;
      else cout << "not available"<<endl;
    }
  }

  return 0;
}
