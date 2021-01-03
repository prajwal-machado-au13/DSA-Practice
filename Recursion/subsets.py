def subsets(nums):
    results=[]
    dfs(sorted(nums),0,[],results)
    print(results)
def dfs(nums,index,path,res):
    res.append(path)
    for i in range(index,len(nums)):
        dfs(nums,i+1,path+[nums[i]],res)

if __name__ == "__main__":
    nums=[1,2]
   
    print(subsets(nums))
    