
// Definition for singly-linked list.
class ListNode {
    val: number
    next: ListNode | null
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.next = (next===undefined ? null : next)
    }
}


const mergeTwoLists = (list1: ListNode | null, list2: ListNode | null): ListNode | null => {
    let dummy = new ListNode();
    const mergedList = dummy;

    while(list1 && list2) {
        if (list1.val < list2.val) {
            dummy.next = list1;
            list1 = list1.next;
        } else {
            dummy.next = list2;
            list2 = list2.next;
        }

        dummy = dummy.next;
    }

    dummy.next = list1 || list2;

    return mergedList.next;
};