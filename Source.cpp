#include<iostream>
#include<queue>
using namespace std;
template<typename T>
struct Node
{
	Node<T>* left;
	Node<T>* right;
	T info; 
public:
	Node()
	{
		left = right = NULL;
	}
	Node(T val)
	{
		info = val;
		left = right = NULL;
	}
};
template<typename T>
class BST
{
	Node<T>* root;
	template<typename T>
	void LVR(Node<T>* root)
	{
		if (root == NULL)
			return;
		LVR(root->left);
		cout << root->info << ":";
		LVR(root->right);
	}
public:
	BST()
	{
		root = 0;
	}
	void insert(T key);
	void remove(T key);
	bool search(T key);
	void inOrder();
	Node<T>* recursiveInsert(Node<T>* p, T key);
	bool recursiveSearch(Node<T>* p, T key);
	int parent(Node<T>* p, T key);
	int getParent(T key);
	void printLevelOrder();
	void inOrderSucPre(T key);
	Node<T>* getSibling(Node<T>* p, T key)
	{

		if (p == NULL && p->data == key)
			return NULL;
		if (p->left!=NULL && p->left->info == key)
			return p->right;
		 if (p->right!=NULL && p->right->info == key)
			return p->left;

		if (key > p->info)
			getSibling(p->right, key);
		else if(key < p->info)
			getSibling(p->left, key);
	}
	Node<T>*fingSibling(T key)
	{
		return getSibling(root, key);
	}
};
template<typename T>
void BST<T>::insert(T key)
{
	Node<T>* p = root;
	Node<T>* child = new Node<T>(key);
	if (!root)
	{
		root = child;
		return;
	}
	while (p != NULL)
	{
		if (key < p->info)
		{
			if (p->left != NULL)
				p = p->left;
			else
			{
				p->left = child;
				return;
			}
		}
		else
		{
			if (p->right != NULL)
				p = p->right;
			else
			{
				p->right = child;
				return;
			}
		}
	}
}
template<typename T>
void BST<T>::remove(T key)
{
	Node<T>* p = root;
	Node<T>* prev = root;
	while (p != 0)
	{
		if (p->info == key)
		{
			if (p->left == 0 && p->right == 0)
			{
				if (prev->left == p)
					prev->left = 0;
				else
					prev->right = 0;
				delete p;
			}
			if (p->left && !p->right || p->right && !p->left)
			{

			}


		}
		else if (key < p->info)
		{
			prev = p;
			p = p->left;
		}
		else
		{
			prev = p;
			p = p->right;
		}

	}
	
}
template<typename T>
bool BST<T>::search(T key)
{
	Node<T>* p = root;
	while (p != nullptr)
	{
		if (p->info == key)
			return true;
		else if (key < p->info)
			p = p->left;
		else
			p = p->right;
	}
	return false;

}
template<typename T>
void BST<T>::inOrder()
{
	LVR(root);
}
template<typename T>
Node<T>* BST<T>::recursiveInsert(Node<T>* p, T key)
{
	Node<T>* newNode = new Node<T>(key);
	if (p == NULL)
		return newNode;
	if (key<p->info)
		p->left = recursiveInsert(p->left, key);
	else if (key>p->info)
		p->right = recursiveInsert(p->right, key);
	else
		return p;
	
}
template<typename T>
bool BST<T>::recursiveSearch(Node<T>* p, T key)
{
	if (p == NULL)
		return false;
	if (p->info == key)
		return true;
	else if (key < p->info)
		recursiveSearch(p->left, key);
	else if (key > p->info)
		recursiveSearch(p->right, key);
}
template<typename T>
int BST<T>::parent(Node<T>* p, T key)
{	
	if (p == NULL || p->info == key)
		return -1;
	Node<T>* parent = p;
	while (p != NULL)
	{
		if (key == p->info)
		{
			return parent->info;
		}
		else if (key < p->info)
		{
			parent = p;
			p = p->left;
		}
		else if (key > p->info)
		{
			parent = p;
			p = p->right;
		}
	}
}
template<typename T>
int BST<T>::getParent(T key)
{
	return parent(root,key);
}
template<typename T>
void BST<T>::printLevelOrder()
{
	if (root == NULL)
		return;
	queue<Node<T>*>q;
	q.push(root);
	q.push(NULL);
	while (!q.empty())
	{
		Node<T>* node = q.front();
		q.pop();
		if (node != NULL)
		{
			cout << node->info << " ";
			if (node->left)
				q.push(node->left);
			else if (node->right)
				q.push(node->right);
		}
		else if (!q.empty())
		{
			q.push(NULL);
		}
	}

}
//template<typename T>
//void BST<T>::inOrderSucPre(T key)
//{
//	// Base case
//	if (root == NULL)  return;
//
//	// If key is present at root
//	if (root->key == key)
//	{
//		// the maximum value in left subtree is predecessor
//		if (root->left != NULL)
//		{
//			Node* tmp = root->left;
//			while (tmp->right)
//				tmp = tmp->right;
//			pre = tmp;
//		}
//
//		// the minimum value in right subtree is successor
//		if (root->right != NULL)
//		{
//			Node* tmp = root->right;
//			while (tmp->left)
//				tmp = tmp->left;
//			suc = tmp;
//		}
//		return;
//	}
//
//	// If key is smaller than root's key, go to left subtree
//	if (root->key > key)
//	{
//		suc = root;
//		findPreSuc(root->left,key);
//	}
//	else // go to right subtree
//	{
//		pre = root;
//		findPreSuc(root->right, pre, suc, key);
//	}
//}

int main()
{
	BST<int> b1;
	b1.insert(50);
	b1.insert(30);
	b1.insert(20);
	b1.insert(40);
	b1.insert(60);
	b1.insert(55);
	b1.insert(70);
	//b1.printLevelOrder();
	b1.inOrder();
	cout << b1.getParent(40);
//	cout << b1.fingSibling(20);
	//cout<<b1.getParent(20);
	//cout<<b1.search(1);

	
	

}