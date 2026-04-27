import React, { useEffect, useState } from 'react';

const Users = () => {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);

  const loadData = () => {
    const codespace = process.env.REACT_APP_CODESPACE_NAME;
    const endpoint = codespace
      ? `https://${codespace}-8000.app.github.dev/api/users/`
      : 'http://localhost:8000/api/users/';

    console.log('REST API endpoint (Users):', endpoint);
    setLoading(true);

    fetch(endpoint)
      .then((res) => res.json())
      .then((json) => {
        const results = Array.isArray(json)
          ? json
          : Array.isArray(json.results)
          ? json.results
          : [];
        setData(results);
        setLoading(false);
        console.log('Fetched Users:', results);
      })
      .catch((err) => {
        console.error('Error fetching Users:', err);
        setLoading(false);
      });
  };

  useEffect(() => {
    loadData();
  }, []);

  const renderTable = () => {
    if (loading) {
      return <div className="text-center text-muted py-4">Loading users...</div>;
    }

    if (!data.length) {
      return <div className="text-center text-muted py-4">No users available.</div>;
    }

    const headers = Object.keys(data[0]);
    return (
      <div className="table-responsive">
        <table className="table table-striped table-bordered table-hover align-middle mb-0">
          <thead>
            <tr>
              {headers.map((key) => (
                <th key={key} className="text-center text-uppercase small">
                  {key}
                </th>
              ))}
            </tr>
          </thead>
          <tbody>
            {data.map((item, idx) => (
              <tr key={item.id || idx}>
                {headers.map((key) => (
                  <td key={key} className="text-center">
                    {typeof item[key] === 'object' ? JSON.stringify(item[key]) : item[key]}
                  </td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    );
  };

  return (
    <div className="card mb-4 shadow-sm">
      <div className="card-header bg-white border-0 d-flex justify-content-between align-items-center">
        <h2 className="card-title mb-0 text-warning">Users</h2>
        <button type="button" className="btn btn-primary btn-sm" onClick={loadData}>
          Refresh
        </button>
      </div>
      <div className="card-body">{renderTable()}</div>
    </div>
  );
};
export default Users;
