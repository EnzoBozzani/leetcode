function productExceptSelf(nums: number[]): number[] {
    const products = nums.map((num, index) => {
        let product = 1;
        for (let i = 0; i < nums.length; i++) {
            if (i !== index) {
                product *= nums[i];
            };
        };
        return product;
    });
    return products;
};