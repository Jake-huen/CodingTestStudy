def post(preorder,inorder,answer):
    if len(preorder)==0 or len(inorder)==0:
        return answer
    else:
        node = preorder[0]
        node_index = inorder.index(node)
        inorder_left = inorder[:node_index]
        inorder_right = inorder[node_index+1:]
        left_length = len(inorder_left)
        preorder_left=preorder[1:left_length+1]
        preorder_right=preorder[left_length+1:]
        answer.insert(0,node)
        post(preorder_right,inorder_right,answer)
        post(preorder_left,inorder_left,answer)
        return answer


while True:
    try:
        preorder, inorder = map(list, input().split())
        answer=list()
        ans = post(preorder,inorder,answer)
        print("".join(ans))
    except EOFError:
        break
