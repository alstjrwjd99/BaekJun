const solution = (book_time) => {
    let arr = [];
    const getTime = (value) => {
      const [h, m] = value.split(':');
      return +h * 60 + +m;
    };

    book_time.map((v) => v.map((v2) => getTime(v2)))
      .sort((a, b) => a[0] - b[0])
      .map((v) => {
        if (arr.length === 0) return arr.push(v);

        for (let a = 0; a <= arr.length; a++) {
          if (arr[a][arr[a].length - 1] + 10 <= v[0]) return arr[a].push(...v);
          if (!arr[a + 1]) return arr.push(v);
        }
      });

    return arr.length;
  };