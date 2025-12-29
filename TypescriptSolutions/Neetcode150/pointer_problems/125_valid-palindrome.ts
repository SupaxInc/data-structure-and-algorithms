const isPalindrome = (s: string): boolean => {
    let l = 0;
    let r = s.length - 1;

    const isAlnum = (c: string): boolean =>  /[a-z0-9]/i.test(c);

    while (l < r) {
        while (l < r && !isAlnum(s[l])) l++;
        while (l < r && !isAlnum(s[r])) r--;

        if (s[l].toLowerCase() !== s[r].toLowerCase()) return false;

        l++;
        r--;
    }

    return true;
};