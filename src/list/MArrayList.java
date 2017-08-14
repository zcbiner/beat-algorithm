package list;

/**
 * Created by zhong on 2017/8/4.
 * 数组实现
 *
 * 线性表是最基本、最简单、也是最常用的一种数据结构。线性表中数据元素之间的
 * 关系是一对一的关系，即除了第一个和最后一个数据元素之外，其它数据元素都是首尾相接的。线性表有
 * 两种存储方式，一种是顺序存储结构，另一种是链式存储结构。我们常用的数组就是一种典型的顺序存储
 * 结构。
 */
public class MArrayList<T> {
    public static final int DEFAULT_CAPATICY = 10;
    private T[] items;
    private int size = 0;


    public T get(int index) {
        if (index < 0 || index > size) {
            throw new ArrayIndexOutOfBoundsException("index illegal");
        }

        return items[index];
    }

    public void set(int index, T data) {
        if (data == null) {
            throw new NullPointerException("data can not null");
        }

        if (index < 0 || index > size) {
            throw new ArrayIndexOutOfBoundsException("index illegal");
        }

        items[index] = data;
    }

    public void add(T data) {
        add(size, data);
    }

    public void add(int index, T data) {
        if (items.length == size) {
            resizeCapaticy(size*2 + 1);
        }

        for (int i = size; i > index ; i--) {
            items[i] = items[i - 1];
        }
        items[index] = data;
        size++;
    }

    public void remove(int index) {
        if (index < 0 || index > size) {
            throw new ArrayIndexOutOfBoundsException("can not remove");
        }

        for (int i = index; i < size; i++) {
            items[i] = items[i + 1];
        }
        size--;
    }

    private void resizeCapaticy(int newCapaticy) {
        if (newCapaticy <= size) {
            return;
        }

        T[] newItems = (T[]) new Object[newCapaticy];
        for (int i = 0; i < size; i++) {
            newItems[i] = items[i];
        }
        items = newItems;
    }
}
