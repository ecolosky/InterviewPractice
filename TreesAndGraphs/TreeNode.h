#ifndef NODE_H
#define NODE_H
#include <iostream>

template<class T>
class Node{
  public:
    Node();
    Node(const T& item, Node<T>* ptrLeft = NULL, Node<T>* ptrRight = NULL,Node<T>* ptrRoot = NULL);
  private:
    Node<T>* left;
    Node<T>* right;
    Node<T>* root;

};
#endif
