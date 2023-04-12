// https://fakerapi.it/en
const objects = ['users', 'books', 'persons'];

const fetchFakerAPI = async () => {
  const res = await Promise.all(
    objects.map(async obj => {
      const res = await fetch(
        `https://fakerapi.it/api/v1/${obj}?_quantity=1`
      );
      const data = await res.json()
      const obj_two = {
        ...data.data
      }
      return obj_two;
    })
  );
  const data = res;
  const finalObj = {
    'user': data[0]['0'],
    'book': data[1]['0'],
    'person': data[2]['0']
  }
  console.log(finalObj)
  return finalObj
}

fetchFakerAPI()