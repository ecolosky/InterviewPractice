#include <iostream>
#include <iomanip>
#include <vector>

class Node{
private:
  int val;
public:
  // pointers made public for easy navigation
  Node* left = NULL;
  Node* right = NULL;
  Node* root = NULL;
  //  Constructors of Node
  Node(const int& data, Node* l, Node* r, Node* root){
    this->left = l;
    this->right = r;
    this->root = root;
    this->val = data;
  }
  Node(const int& data){
    this->val = data;
  }
  // append child methods
  void appendRight(Node* child){
    this->right = child;
    child->root = this;
  }
  void appendLeft(Node* child){
    this->left = child;
    child->root = this;
  }
  void printVal(){
    int i = this->val;
    std::cout << i<< std::endl;
  }
  int getVal(){
    return this->val;
  }
};

void printTree(Node* p, int indent=0)
{
    if(p != NULL) {
        std::cout<< p->getVal() << std::endl;
        if(p->left) printTree(p->left, indent+4);
        if(p->right) printTree(p->right, indent+4);
        if (indent) {
            std::cout << std::setw(indent) << ' ';
        }

    }
}
bool validBST(Node* root){
  Node* ptr = root;
  bool rtn = true;
  if(ptr != NULL){
    rtn = validBST(ptr->left);
    if(ptr->left != NULL){
      if(ptr->getVal()<ptr->left->getVal()){
        return false;
      }
    }
    if(ptr->right != NULL){
      if(ptr->getVal() > ptr->right->getVal()){
        return false;
      }
    }
    if(rtn == false){
      return false;
    }
    rtn = validBST(ptr->right);
  }
  return rtn;
}
Node* nextNode(Node* ptr){
  if(ptr->right){
    return ptr->right;
  }
  if(ptr->root){
    return ptr->root;
  }
  else{
    ptr = NULL;
    return ptr;
  }
}

int main() {
  /* code */
  Node l2 (12);
  Node r2 (17);
  Node l1 (1);
  Node r1 (7);
  Node l (4);
  Node r (14);
  Node rt (9,&l,&r,NULL);
  l.appendLeft(&l1);
  l.appendRight(&r1);
  r.appendLeft(&l2);
  r.appendRight(&r2);
  bool resp = validBST(&rt);
  std::cout <<  "Valid BST ? "<< resp << std::endl;
  Node* ptr = nextNode(&l);
  std::cout <<  "Next Node in Tree: "<< ptr->getVal() << std::endl;
  return 0;
}
