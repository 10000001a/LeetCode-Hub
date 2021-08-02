/**
 * Definition for Employee.
 * function Employee(id, importance, subordinates) {
 *     this.id = id;
 *     this.importance = importance;
 *     this.subordinates = subordinates;
 * }
 */

/**
 * @param {Employee[]} employees
 * @param {number} id
 * @return {number}
 */
var GetImportance = function(employees, id) {
  const employee = employees.find(employee => employee.id === id);
  
  const queue = [employee];
  
  let answer = 0;
  
  while (queue.length > 0) {
    const {importance, subordinates} = queue.shift();
    
    answer += importance;
    
    subordinates.forEach(id => queue.push(employees.find(employee => employee.id === id)));
  }
  
  return answer;
};