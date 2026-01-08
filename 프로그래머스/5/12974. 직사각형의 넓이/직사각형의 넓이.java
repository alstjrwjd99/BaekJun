import java.util.*;

class Solution {

    static class Event {
        long x;
        int y1, y2;   // index in compressed coords (inclusive range on segments: [y1, y2-1])
        int delta;    // +1 add, -1 remove
        Event(long x, int y1, int y2, int delta) {
            this.x = x; this.y1 = y1; this.y2 = y2; this.delta = delta;
        }
    }

    static class SegTree {
        int nSeg;          // number of y-segments = ys.length - 1
        int[] cover;       // cover count
        long[] len;        // covered length
        long[] ys;         // coordinate values

        SegTree(long[] ys) {
            this.ys = ys;
            this.nSeg = ys.length - 1;
            int size = 4 * Math.max(1, nSeg);
            cover = new int[size];
            len = new long[size];
        }

        void update(int ql, int qr, int delta) {
            if (ql > qr) return;
            update(1, 0, nSeg - 1, ql, qr, delta);
        }

        private void update(int node, int l, int r, int ql, int qr, int delta) {
            if (qr < l || r < ql) return;
            if (ql <= l && r <= qr) {
                cover[node] += delta;
                pull(node, l, r);
                return;
            }
            int mid = (l + r) >>> 1;
            update(node << 1, l, mid, ql, qr, delta);
            update(node << 1 | 1, mid + 1, r, ql, qr, delta);
            pull(node, l, r);
        }

        private void pull(int node, int l, int r) {
            if (cover[node] > 0) {
                // fully covered
                len[node] = ys[r + 1] - ys[l];
            } else {
                if (l == r) len[node] = 0;
                else len[node] = len[node << 1] + len[node << 1 | 1];
            }
        }

        long coveredLength() {
            return len[1];
        }
    }

    public long solution(int[][] rectangles) {
        int n = rectangles.length;

        // 1) collect all y
        long[] allY = new long[2 * n];
        for (int i = 0; i < n; i++) {
            allY[2 * i] = rectangles[i][1];
            allY[2 * i + 1] = rectangles[i][3];
        }
        Arrays.sort(allY);

        // unique
        long[] ys = new long[allY.length];
        int m = 0;
        for (long v : allY) {
            if (m == 0 || ys[m - 1] != v) ys[m++] = v;
        }
        ys = Arrays.copyOf(ys, m);

        // map y -> index
        // ys length up to 2e5, binarySearch per event is fine
        List<Event> events = new ArrayList<>(2 * n);
        for (int i = 0; i < n; i++) {
            long x1 = rectangles[i][0];
            long y1 = rectangles[i][1];
            long x2 = rectangles[i][2];
            long y2 = rectangles[i][3];

            int iy1 = Arrays.binarySearch(ys, y1);
            int iy2 = Arrays.binarySearch(ys, y2);

            // segment indices are [0 .. ys.length-2], update [iy1 .. iy2-1]
            events.add(new Event(x1, iy1, iy2, +1));
            events.add(new Event(x2, iy1, iy2, -1));
        }

        // sort by x
        events.sort(Comparator.comparingLong(e -> e.x));

        // 2) sweep
        SegTree st = new SegTree(ys);

        long area = 0;
        long prevX = events.get(0).x;
        int i = 0;
        while (i < events.size()) {
            long curX = events.get(i).x;
            long dx = curX - prevX;
            if (dx != 0) {
                area += st.coveredLength() * dx;
                prevX = curX;
            }

            // process all events at curX
            while (i < events.size() && events.get(i).x == curX) {
                Event e = events.get(i++);
                st.update(e.y1, e.y2 - 1, e.delta);
            }
        }

        return area;
    }
}