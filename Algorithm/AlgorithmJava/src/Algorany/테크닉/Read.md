# 순열과 조합을 구현하는 방법
백트래킹 개념을 이용하여 visited 배열을 이용
## 순열, 중복순열, 조합, 중복조합

- String str : 주어진 조건(필요시 배열로 처리)
- int r : 주어진 조건에서 선택할 개수 (ex. 5개 중 2개를 뽑는다, r=2)
- List<Integer> list : 각 경우를 저장할 리스트
- boolean[] visited : 순열과 조합에서 주어진 조건 중 중복해서 뽑지않게 체크 용도
  (중복 허용한다면 필요없음)
- String temp : 각 상황마다 뽑힌 것들을 임시로 저장할 변수
  (필요시 배열로도 가능)
- int count : 각 상황의 결과의 개수가 몇개인지 확인할 용도

### 1. 순열
```java
static void perm(String str, String temp, int r){
    if (r == 0) {
        int num = Integer.parseInt(temp);
        list.add(num);
        count++;
        return;
    }

    for (int i = 0; i < str.length(); i++) {
        if(!visited[i]){
            temp += str.charAt(i);
            visited[i] = true;
            perm(str, temp, r - 1);
            visited[i] = false;
            temp = temp.substring(0, temp.length() - 1);
        }
    }
}
```

### 2. 중복순열
```java
static void dupPerm(String str, String temp, int r) {
  if (r == 0) {
    int num = Integer.parseInt(temp);
    list.add(num);
    count++;
    return;
  }

  for (int i = 0; i < str.length(); i++) {
    temp += str.charAt(i);
    dupPerm(str, temp, r - 1);
    temp = temp.substring(0, temp.length() - 1);
  }
}
```

### 3. 조합
```java
static void comb(String str, String temp, int start, int r) {
  if (r == 0) {
    int num = Integer.parseInt(temp);
    list.add(num);
    count++;
    return;
  }

  for (int i = start; i < str.length(); i++) {
    if (!visited[i]) {
      temp += str.charAt(i);
      visited[i] = true;
      comb(str, temp, i + 1, r - 1);
      visited[i] = false;
      temp = temp.substring(0, temp.length() - 1);
    }
  }
}
```

### 4. 중복 조합
```java
static void dupComb(String str, String temp, int start, int r) {
  if (r == 0) {
    int num = Integer.parseInt(temp);
    list.add(num);
    count++;
    return;
  }

  for (int i = start; i < str.length(); i++) {
    temp += str.charAt(i);
    dupComb(str, temp, i, r - 1);
    temp = temp.substring(0, temp.length() - 1);
  }
}
```
