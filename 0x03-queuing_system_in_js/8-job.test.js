import createPushNotificationsJobs from './8-job';
const kue = require('kue');
const { expect } = require('chai');

describe('createPushNotificationsJobs', () => {
  let queue;

  before(() => {
    queue = kue.createQueue();
    queue.testMode.enter();
  });

  afterEach(() => {
    queue.testMode.clear();
  });

  after(() => {
    queue.testMode.exit();
  });

  it('should create jobs in the queue', () => {
    const jobs = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 0001 to verify your account'
      },
      {
        phoneNumber: '4153518781',
        message: 'This is the code 0022 to verify your account'
      }
    ];

    createPushNotificationsJobs(jobs, queue);

    const jobCount = queue.testMode.jobs.length;
    expect(jobCount).to.equal(2);

    const jobData = queue.testMode.jobs[0].data;
    expect(jobData).to.deep.equal(jobs[0]);
  });

  it('should throw an error if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs({}, queue)).to.throw('Jobs is not an array');
  });
});
