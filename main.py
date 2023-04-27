import hg
import pr_d
import eig
l=["page1.html","page2.html","page3.html","page4.html"]
##To parse the HTML File, and convert it to the transition matrix
A=hg.trans_mat(l)
# print("Transition Matrix A is::")
# print(A)
# print('------------------')
# ##Dynamic systems 
# l=pr_d.pr(A,4)

# ##Eigen Vector Method
# print('---------------------')
# pg=eig.pgr(A)

