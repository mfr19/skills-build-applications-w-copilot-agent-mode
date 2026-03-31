import React, { useEffect, useState } from 'react';

const Workouts = () => {
  const [data, setData] = useState([]);
  useEffect(() => {
    const codespace = process.env.REACT_APP_CODESPACE_NAME;
    const endpoint = `https://${codespace}-8000.app.github.dev/api/workouts/`;
    console.log('Fetching Workouts from:', endpoint);
    fetch(endpoint)
      .then(res => res.json())
      .then(json => {
        const results = json.results || json;
        setData(results);
        console.log('Fetched Workouts:', results);
      })
      .catch(err => console.error('Error fetching Workouts:', err));
  }, []);
  return (
    <div className="card mb-4 shadow-sm">
      <div className="card-body">
        <h2 className="card-title mb-4 text-danger display-6">Workouts</h2>
        <div className="table-responsive">
          <table className="table table-striped table-bordered align-middle">
            <thead>
              <tr>
                {data[0] && Object.keys(data[0]).map((key) => (
                  <th key={key} className="text-center">{key}</th>
                ))}
              </tr>
            </thead>
            <tbody>
              {data.map((item, idx) => (
                <tr key={item.id || idx}>
                  {Object.values(item).map((val, i) => (
                    <td key={i} className="text-center">{typeof val === 'object' ? JSON.stringify(val) : val}</td>
                  ))}
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};
export default Workouts;
