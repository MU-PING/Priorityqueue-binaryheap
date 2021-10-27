# PriorityQueue_BinaryHeap
## 程式簡介
### 簡述
* 透過Max( Min )Binary Heap 實作  Priority-Queue，屬於「資料結構」的實作

* 此程式使用 Linked List ( Python 中的 list ) 實作 Binary Heap

* 相較 Linked List，若使用 Array 實作，程式效能會較高 
### 範例圖 
![](https://i.imgur.com/07oIVHQ.jpg)
## Binary Heap 、 Priority-Queue 資料結構
### Binary Heap簡介
* Heap 是一種**特別**的樹。滿足以下特性：
    * 任意節點P和C，若P是C的母節點，那麼P的值會小於等於（或大於等於）C的值。
    
        * 「大於」時，稱為最大堆積（max heap）
        * 「小於」時，稱為最小堆積（min heap）       
        
* Heap 大致分為以下幾種：
    * 基本型
        * Binary Heap( 二元堆積 )
        * Other
    * 進階型
        * Leftist Heap ( 左傾堆積 )
        * Binomial Heap ( 二項式堆積 )
        * Fibonacci Heap ( 費式堆積 )
        * Pairing Heap ( 成對堆積 )
        * Symmetric Min-Max Heap ( 對稱式最小-最大堆積 )
        * Interval Heap ( 區間堆積 )
        * Other
* Binary Heap 屬於 Heap 最基本的實現方式，由於普遍性，當不加限定時：Heap == Binary Heap
* Binary Heap 除滿足 Heap的基本特性，同時是一顆「完全二元樹」

![](https://i.imgur.com/wRdKKwb.png)
### Priority-Queue簡介
* 一種抽象資料類型。Priority-Queue中的每個元素都有各自的權重
    * 權重越高的元素最先被服務(或是有較大機率被服務)
    * 權重越低的元素最後被服務(或是有較小機率被服務)
    
* Priority-Queue往往使用 Heap 來實現，上述提到的「基本型」或「進階型」 Heap 都可實作



更多細節可參考：http://alrightchiu.github.io/SecondRound/priority-queuebinary-heap.html
