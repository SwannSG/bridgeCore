// Distribution combinations

var dc = {
    SUIT_COMBO: [['S', 'H', 'D', 'C'], ['S', 'H', 'C', 'D'], ['S', 'D', 'H', 'C'], ['S', 'D', 'C', 'H'], ['S', 'C', 'H', 'D'], ['S', 'C', 'D', 'H'], ['H', 'S', 'D', 'C'], ['H', 'S', 'C', 'D'], ['H', 'D', 'S', 'C'], ['H', 'D', 'C', 'S'], ['H', 'C', 'S', 'D'], ['H', 'C', 'D', 'S'], ['D', 'S', 'H', 'C'], ['D', 'S', 'C', 'H'], ['D', 'H', 'S', 'C'], ['D', 'H', 'C', 'S'], ['D', 'C', 'S', 'H'], ['D', 'C', 'H', 'S'], ['C', 'S', 'H', 'D'], ['C', 'S', 'D', 'H'], ['C', 'H', 'S', 'D'], ['C', 'H', 'D', 'S'], ['C', 'D', 'S', 'H'], ['C', 'D', 'H', 'S']],

    _flatten(arr) {
        return [].concat.apply([], arr)
    },

    _product(...sets) {
        return sets.reduce((acc, set) => this._flatten(acc.map(x => set.map(y => [ ...x, y ]))), [[]]);
    },

    // getDistributions(constraints={S: {min:3,max:5}, H:{min:3,max:5}, D:{min:1,max:5}, C:{min:1,max:5}}) {
    getDistributions(constraints={S: {min:0,max:13}, H:{min:0,max:13}, D:{min:0,max:13}, C:{min:0,max:13}}) {
        // generate a set of distribution solutions
        // constraints={S: {min:0,max:13}, H:{min:0,max:13}, D:{min:0,max:13}, C:{min:0,max:13}}
        if (constraints.S.min + constraints.H.min + constraints.D.min + constraints.C.min > 13) {
            return 'Error: constraints.S.min + constraints.H.min + constraints.D.min + constraints.C.min > 13';
        }
        var values = {};
        values['S'] = this._fillArray(constraints.S.min, constraints.S.max);
        values['H'] = this._fillArray(constraints.H.min, constraints.H.max);
        values['D'] = this._fillArray(constraints.D.min, constraints.D.max);
        values['C'] = this._fillArray(constraints.C.min, constraints.C.max);

        var result = [];
        var prodArray;
        var item;
        for (var i=0; i < this.SUIT_COMBO.length; i++) {
            // loop thro' each suit combination in SUIT_COMBO
            prodArray = this._product(values[this.SUIT_COMBO[i][0]],
                                 values[this.SUIT_COMBO[i][1]],
                                values[this.SUIT_COMBO[i][2]],
                                values[this.SUIT_COMBO[i][3]]);

            prodArray.forEach(
                function isSolution(item) {
                    if (item[0] + item[1] + item[2] + item[3] === 13) {
                        // valid solution
                        result.push(this._setOrder(item, this.SUIT_COMBO[i]));
                    }
                },
                this
            )
        }
        return this._rmvDuplArray(result);
    },

    _setOrder(arr, suitOrder) {
        // arrange arr in standard suit order 'S-H-D-C'
        return  arr[suitOrder.indexOf('S')] + '-' +
                arr[suitOrder.indexOf('H')] + '-' +
                arr[suitOrder.indexOf('D')] + '-' +
                arr[suitOrder.indexOf('C')];
    },

    _fillArray(startInt, endInt) {
        // fill array with integers startInt to endInt
        let arr = [];
        let item = startInt;
        while (item <= endInt) {
            arr.push(item);
            item++;
        }
        return arr;
    },

    _rmvDuplArray(arr) {
        // remove duplicates from array
        let result=[]
        let temp = {}
        for (i=0; i<arr.length; i++) {
            // assign property name to any value
            temp[arr[i]] = 0;
        }
        for (x in temp) {
          result.push(x);
        }
        return result;
    }
}
